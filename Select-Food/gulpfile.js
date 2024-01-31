var merge = require("merge-stream");
var gulp = require("gulp");
var browserify = require("browserify");
var babelify = require("babelify");
var source = require("vinyl-source-stream");
var sourcemaps = require("gulp-sourcemaps");
var buffer = require('vinyl-buffer');
var uglify = require('gulp-uglify');
var glob = require('glob');
var path = require('path');

gulp.task("buildjs", async () => {
    var files = glob.sync("./source/js/*.js");
    return merge(files.map(function(file) {
        return browserify({entries: file, debug:true})
        .transform(babelify, {sourceMaps:true})
        .bundle()
        .pipe(source(path.basename(file, ".js") + ".js"))
        .pipe(buffer())
        .pipe(sourcemaps.init({loadMaps: true}))
        .pipe(uglify())
        .pipe(sourcemaps.write('./'))
        .pipe(gulp.dest("/var/www/html/js"));
    }));
});

gulp.task("copyhtmls", async () => {
    return gulp.src("./source/*.html")
        .pipe(gulp.dest("/var/www/html"));
});

gulp.task("copycsss", async () => {
    return gulp.src("./source/css/*.css")
        .pipe(gulp.dest("/var/www/html/css"));
});

gulp.task("watch", async () => {
    gulp.watch("source/js/*.js",    gulp.series("buildjs"));
    gulp.watch("source/*.html",     gulp.series("copyhtmls"));
    gulp.watch("source/css/*.css",  gulp.series("copycsss"));
});

gulp.task("default", gulp.series(
    "buildjs",
    "copyhtmls",
    "copycsss",
    "watch"));