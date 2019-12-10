-- A palindromic number reads the same both ways. The largest palindrome 
-- made from the product of two 2-digit numbers is 9009 = 91 × 99.
-- Find the largest palindrome made from the product of two 3-digit numbers.
import Text.Printf

smallest = 10001 :: Int
biggest = 999^2 :: Int

digit_count :: Int -> Int
digit_count n = ceiling $ logBase 10 (fromIntegral n)


---- Cartesian Product ----
zipSingle x [] = []
zipSingle x (y:ys) = (x, y):(zipSingle x ys)

cartesian [] _ = []
cartesian _ [] = []
cartesian (x:xs) ys = (zipSingle x ys) ++ cartesian xs ys
---- End Cartesian Product ----



main = do
    printf "%i\n" smallest
    printf "%i\n" biggest

    printf "%i\n" (digit_count smallest)
    printf "%i\n" (digit_count biggest)
    
    let c =  cartesian [1..2] [3..4]
    putStrLn $ show $ c
