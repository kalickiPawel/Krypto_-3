package com.company;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;

import demo.ECCelerateDemo;
import iaik.security.ec.common.SecurityStrength;
import iaik.security.ec.errorhandling.InvalidCurveException;
import iaik.security.ec.math.common.Pair;
import iaik.security.ec.math.curve.*;
import iaik.security.ec.math.field.GenericFieldElement;
import iaik.utils.Util;
import demo.math.bls.BLSDemo;

public class Main {

    public static void main(String[] args) {
        // MileStone #1
        BLSDemo demo = new BLSDemo();
        demo.run();

        // MileStone #2
        pairingProtocol();
        pairingtests();

        // MileStone #3
        waters_3b();
    }

    public static void waters_3b() {
        //a -inicjalizacja
        int size = 160;
        // int size = 256;
        // int size = 384;
        // int size = 512;
        // int size = 638;
        // inicjalizacja odwzorowania typu 3
        final Pairing pair3 = AtePairingOverBarretoNaehrigCurveFactory.getPairing(PairingTypes.TYPE_3, size);
        EllipticCurve curve1 = pair3.getGroup1();
        EllipticCurve curve2 = pair3.getGroup2();
        //b -liczby losowe
        final SecureRandom random = SecurityStrength.getSecureRandom(SecurityStrength.getSecurityStrength(curve1.getField().getFieldSize()));

        //tworzenie liczby losowej
        BigInteger s_TA = new BigInteger(size - 1, random);
        //c -pobieranie generatora dla danej krzywej
        ECPoint P = curve1.getGenerator();
        ECPoint Q = curve2.getGenerator();
        //mnożenie punktu przez skalar
        //jak potrzebujemy losowy punkt na krzywej, to losujemy punkt i mnożymy przez skalar
        ECPoint P_0 = P.multiplyPoint(s_TA);
        ECPoint Q_0 = Q.multiplyPoint(s_TA);
        //obliczanie odwzorowania
        GenericFieldElement e1 = pair3.pair(P, Q_0);
        GenericFieldElement e2 = pair3.pair(P_0, Q);
        System.out.println(e1);
        System.out.println(e2);
        if (e1.equals(e2)) {
            System.out.println("Wszystko działa jak powinno :)");
        }
        //obliczanie skrótów i tworzenie z nich liczby BigInt
        // jak chcemy jako wyjście funkcji skrótu otrzymać punkt to przemnażamy przez generator
        try {
            String tmp = "tutaj dowolna wiadomość";
            tmp += P_0.toString();
            tmp += e1.toString();
            MessageDigest md = MessageDigest.getInstance("SHA-512");
            byte[] messageDigest = md.digest(tmp.getBytes());
            BigInteger result = new BigInteger(1, messageDigest);
            ECPoint result2 = P.multiplyPoint(result);
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }

    }
    public static void pairingtests() {
        //a -inicjalizacja
        int size = 160;
        // int size = 256;
        // int size = 384;
        // int size = 512;
        // int size = 638;
        // inicjalizacja odwzorowania typu 3
        final Pairing pair3 = AtePairingOverBarretoNaehrigCurveFactory.getPairing(PairingTypes.TYPE_3, size);
        EllipticCurve curve1 = pair3.getGroup1();
        EllipticCurve curve2 = pair3.getGroup2();

        //b -liczby losowe
        final SecureRandom random = SecurityStrength.getSecureRandom(SecurityStrength.getSecurityStrength(curve1.getField().getFieldSize()));

        //tworzenie liczby losowej
        BigInteger s_TA = new BigInteger(size - 1, random);

        //c -pobieranie generatora dla danej krzywej
        ECPoint P = curve1.getGenerator();
        ECPoint Q = curve2.getGenerator();

        //mnożenie punktu przez skalar
        // jak potrzebujemy losowy punkt na krzywej, to losujemy punkt i mnożymy przez skalar
        ECPoint P_0 = P.multiplyPoint(s_TA);
        ECPoint Q_0 = Q.multiplyPoint(s_TA);

        //obliczanie odwzorowania
        GenericFieldElement e1 = pair3.pair(P, Q_0);
        GenericFieldElement e2 = pair3.pair(P_0, Q);
        System.out.println(e1);
        System.out.println(e2);

        if (e1.equals(e2)) {
            System.out.println("Wszystko działa jak powinno :)");
        }

        //obliczanie skrótów i tworzenie z nich liczby BigInt
        // jak chcemy jako wyjście funkcji skrótu otrzymać punkt to przemnażamy przez generator
        try {
            String tmp = "tutaj dowolna wiadomość";
            tmp += P_0.toString();
            tmp += e1.toString();
            MessageDigest md = MessageDigest.getInstance("SHA-512");
            byte[] messageDigest = md.digest(tmp.getBytes());
            BigInteger result = new BigInteger(1, messageDigest);
            ECPoint result2 = P.multiplyPoint(result);
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
    }

    public static void pairingProtocol() {
        int size = 160;
        final Pairing pair3 = AtePairingOverBarretoNaehrigCurveFactory.getPairing(PairingTypes.TYPE_3, size);
        EllipticCurve curve1 = pair3.getGroup1();
        EllipticCurve curve2 = pair3.getGroup2();
        //b -liczby losowe
        final SecureRandom random = SecurityStrength.getSecureRandom(SecurityStrength.getSecurityStrength(curve1.getField().getFieldSize()));

        //tworzenie liczby losowej
        BigInteger s_TA = new BigInteger(size -1, random);
        BigInteger s_TB = new BigInteger(size -1, random);
        BigInteger s_TC = new BigInteger(size -1, random);

        ECPoint P = curve1.getGenerator();
        ECPoint Q = curve2.getGenerator();
        //mnożenie punktu przez skalar
        //jak potrzebujemy losowy punkt na krzywej, to losujemy punkt i mnożymy przez skalar

        ECPoint P_1 = P.multiplyPoint(s_TA);
        ECPoint Q_1 = Q.multiplyPoint(s_TA);

        ECPoint P_2 = P.multiplyPoint(s_TB);
        ECPoint Q_2 = Q.multiplyPoint(s_TB);

        ECPoint P_3 = P.multiplyPoint(s_TC);
        ECPoint Q_3 = Q.multiplyPoint(s_TC);

        //obliczanie odwzorowania
        GenericFieldElement e1 = pair3.pair(P_1, Q_2);
        GenericFieldElement e2 = pair3.pair(P_2, Q_3);
        GenericFieldElement e3 = pair3.pair(P_3, Q_1);

        System.out.println("");
        System.out.println(e1);
        System.out.println(e2);
        System.out.println(e3);

        System.out.println("");
        e1.exponentiate(s_TC);
        e2.exponentiate(s_TA);
        e3.exponentiate(s_TB);

        System.out.println(e1);
        System.out.println(e2);
        System.out.println(e3);

        if (e1.equals(e2)) {System.out.println("Wszystko działa 1-2");}
        if (e2.equals(e3)) {System.out.println("Wszystko działa 2-3");}

    }
}
