-- A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
-- a2 + b2 = c2
-- For example, 32 + 42 = 9 + 16 = 25 = 52.
-- There exists exactly one Pythagorean triplet for which a + b + c = 1000.
-- Find the product abc.

import Data.Foldable


putLn x = (putStrLn . show) x
sqrti x = floor $ sqrt $ fromInteger x

cond x y = let z2 = x*x + y*y
               z = sqrti z2
               iszsquare = z*z == z2
               addupto1000 = x + y + z == 1000
            in iszsquare && addupto1000


showResult x y = do
    putLn x
    putLn y
    let z = sqrti (x^2 + y^2)
    putLn z
    putLn $ x * y * z

main = do
    let allpairs = [(x, y) | x <- [1..999], y <- [x..999]]
    let pit = find (\xy -> cond (fst xy) (snd xy)) allpairs
    case pit of
        Just xy -> showResult (fst xy) (snd xy)
        Nothing -> putLn "Object not Found"

