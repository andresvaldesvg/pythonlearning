# Example 1: Simple if statement
if 5 < 6
  puts "Yes, 5 is less than 6"
  puts "Everybody knows that"
  puts "I am a genius"
end

# Example 2: If-else statement
if 10 > 20
  puts "This will not be printed"
else
  puts "10 is not greater than 20"
end

# Example 3: If-elif-else statement
number = 15
if number < 10
  puts "Number is less than 10"
elsif number == 15
  puts "Number is 15"
else
  puts "Number is greater than 10 but not 15"
end

# Example 4: Nested if statements
age = 18
if age >= 18
  puts "You are an adult"
  if age >= 65
    puts "You are a senior citizen"
  else
    puts "You are not a senior citizen"
  end
else
  puts "You are not an adult"
end
