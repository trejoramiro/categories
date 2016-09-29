module.exports = function(grunt) {
  grunt.initConfig({
    karma: {
      unit: {
        configFile: 'karma-unit.config.js'
      }
    }
  });
  grunt.loadNpmTasks('grunt-karma');
}
