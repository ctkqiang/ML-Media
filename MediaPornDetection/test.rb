gem 'sightengine-ruby'

puts "Please Input Data Directory: "
dir = gets

puts Sightengine.moderate(dir)