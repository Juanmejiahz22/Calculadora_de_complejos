import libcplx as lc
import unittest

class TestCplxOperations(unittest.TestCase):

    def test_sumacplx(self):
        suma = lc.sumacplx((3,2),(-5,5.2))
        self.assertAlmostEqual(suma[0],-2)
        self.assertAlmostEqual(suma[1],7.2)

    def test2_sumacplx(self):
        suma = lc.sumacplx((5,1),(7,10.2))
        self.assertAlmostEqual(suma[0],12)
        self.assertAlmostEqual(suma[1],11.2)

    def test_multicplx(self):
        produ = lc.multicplx((3,2),(-5,5.2))
        self.assertAlmostEqual(produ[0],-2)
        self.assertAlmostEqual(produ[1],7.2)

    def test2_multicplx(self):
        produ = lc.multicplx((5,1),(7,10.2))
        self.assertAlmostEqual(produ[0],24.8)
        self.assertAlmostEqual(produ[1],58)

    def test_restacplx(self):
        res = lc.restacplx((3,2),(-5,5.2))
        self.assertAlmostEqual(res[0],8)
        self.assertAlmostEqual(res[1],-3.2)

    def test2_restacplx(self):
        res = lc.restacplx((5,1),(7,10.2))
        self.assertAlmostEqual(res[0],2)
        self.assertAlmostEqual(res[1],9.2)

    def test_divisioncplx(self):
        div = lc.divicplx((3,2),(-5,5.2))
        self.assertAlmostEqual(div[0],-1.2)
        self.assertAlmostEqual(div[1],-1.03)

    def test2_divisioncplx(self):
        div = lc.divicplx((5,1),(7,10.2))
        self.assertAlmostEqual(div[0],0.29)
        self.assertAlmostEqual(div[1],-0.28)
    
    def test_modulocplx(self):
        mod = lc.modulocplx((3,2))
        self.assertAlmostEqual(mod[0],3.6)
        

    def test2_modulocplx(self):
        mod = lc.modulocplx((5,1))
        self.assertAlmostEqual(mod[0],5.09)
        

    def test_conjugadocplx(self):
        conj = lc.conjugacplx((3,2),(-5,5.2))
        self.assertAlmostEqual(conj[0][1],-2)
        self.assertAlmostEqual(conj[1][1],-5.2)

    def test2_conjugadocplx(self):
        conj = lc.conjugacplx((5,1),(7,10.2))
        self.assertAlmostEqual(conj[0][1],-1)
        self.assertAlmostEqual(conj[1][1],-10.2) 
    
    def test_polarcplx(self):
        pol = lc.polarcplx((3,2))
        self.assertAlmostEqual(pol[0],3.6)
        self.assertAlmostEqual(pol[1],0.8)

    def test2_polarcplx(self):
        pol = lc.polarcplx((5,1))
        self.assertAlmostEqual(pol[0],5.09)
        self.assertAlmostEqual(pol[1],0.19)
    
    def test_cartesianocplx(self):
        car = lc.cartesicplx((3,2))
        self.assertAlmostEqual(car[0],3.0)
        self.assertAlmostEqual(car[1],1.9)

    def test2_cartesianocplx(self):
        car = lc.cartesicplx((5,1))
        self.assertAlmostEqual(car[0],4.9)
        self.assertAlmostEqual(car[1],0.96)

    def test_fasecplx(self):
        fas = lc.fasecplx((3,2))
        self.assertAlmostEqual(fas[0],0.58)
        

    def test2_fasecplx(self):
        fas = lc.fasecplx((5,1))
        self.assertAlmostEqual(fas[0],0.19)
        

    

if __name__ == '__main__':
    unittest.main()