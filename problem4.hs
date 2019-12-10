-- A palindromic number reads the same both ways. The largest palindrome 
-- made from the product of two 2-digit numbers is 9009 = 91 × 99.
-- Find the largest palindrome made from the product of two 3-digit numbers.
import Data.List
import Data.Ord

smallest_factor = 100
biggest_factor = 999


isPalindrome :: Int -> Bool
isPalindrome n = (show n) == (reverse $ show n)


apply x xmin xmax = if xmin <= xmax
                    then [x*xmax, x, xmax]:(apply x xmin (xmax - 1))
                    else []


applyCommutative xmin xmax = if xmin <= xmax
                             then (apply xmax xmin xmax) ++ (applyCommutative xmin (xmax - 1))
                             else []


main = do    
    let c1 = applyCommutative smallest_factor biggest_factor
    let c2 = filter (\x -> isPalindrome $ head x) c1
    putStrLn $ show $ maximumBy (comparing head) c2
