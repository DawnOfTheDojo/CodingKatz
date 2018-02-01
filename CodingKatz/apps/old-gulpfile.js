var gulp = require('gulp');
var sass = require('gulp-sass');
var browserSync = require('browser-sync').create();

// Sync browsers to python runserver
  

gulp.task('sass', function() {
  return gulp
    .src('./LogReg/static/LogReg/sass/*.scss')
    .pipe(sass())
    .pipe(gulp.dest('./css'))
    .pipe(browserSync.stream());
});

gulp.task('serve', ['sass'], function() {
  browserSync.init({
    notify: false,
    localOnly: true,
    proxy: {
      target: 'http://localhost:8000/'
    },
    port: process.env.PORT || 8000
  });

// gulp.task('serve', ['sass'], function() {
//   browserSync.init({
//     server: './'
//   });

  gulp.watch('./LogReg/static/LogReg/sass/*.scss', ['sass']);
  gulp.watch('./**/**/*.html').on('change', browserSync.reload);
});

gulp.task('default', ['serve']);
