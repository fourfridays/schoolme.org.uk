module.exports = function(grunt) {

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        concat: {
            dist: {
                src: ['node_modules/jquery/dist/jquery.slim.min.js', 'node_modules/bootstrap/js/dist/util.js', 'src/schoolme.js'],
                dest: 'dist/js/schoolme.js'
            }
        },
        uglify: {
            options: {
                banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n',
                compress: true
        },
        dist: {
            files: {
                //'/mnt/volume-nyc1-01-part4/static/js/flinthillsparanormal.min.js': ['<%= concat.dist.dest %>'],
                '../static/js/schoolme.min.js': ['<%= concat.dist.dest %>'],
            }
        }
    },
    sass: {                              // Task
      dist: {                            // Target
        files: {                         // Dictionary of files
          //'/mnt/volume-nyc1-01-part4/static/css/flinthillsparanormal.css': 'src/flinthillsparanormal.scss'
          '../static/css/starfish.css': 'src/starfish.scss',
          '../static/css/schoolme.css': 'src/schoolme.scss'
        }
      }
    },
    cssmin: {
      target: {
        files: [{
          expand: true,
          cwd: '../static/css',
          src: ['*.css', '!*.min.css'],
          dest: '../static/css',
          ext: '.min.css'
        }]
      }
    },
    watch: {
      scripts: {
        files: 'src/*.*',
        tasks: ['concat', 'uglify', 'sass'],
        //tasks: ['sass'],
        options: {
          livereload: true
        },
      },
    }
    });

    // Load the plugins
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Default task(s).

    grunt.registerTask('default', ['concat', 'uglify', 'sass', 'cssmin', 'watch']);
    //grunt.registerTask('default', ['sass', 'watch']);

};