module.exports = function(config) {
  config.set({
    frameworks: ['jasmine'], //Informs grunt which test framework to run.
    browsers: ['Firefox'],
    files: [
      'spec/unit/*.js'
    ]
  })
}
