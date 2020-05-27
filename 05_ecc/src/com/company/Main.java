package com.company;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.Date;

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
        String message = "Przykladowy tekst testowy";
        // int size = 160;
        // int size = 256;
        // int size = 384;
        // int size = 512;
        int size = 638;

        // MileStone #1
//        BLSDemo demo = new BLSDemo();
//        demo.run();

        // MileStone #2
//        pairingProtocol();
//        pairingtests(size, message);

        // MileStone #3
        long startTime = System.nanoTime();
        waters_3b(size, message);
        System.out.println("Execution time in nanoseconds: " +(System.nanoTime() - startTime));

    }

    public static void waters_3b(int size, String message) {
        long startTime;
        try {
            final Pairing pair3 = AtePairingOverBarretoNaehrigCurveFactory.getPairing(
                    PairingTypes.TYPE_3, size
            );

            EllipticCurve curve1 = pair3.getGroup1();
            EllipticCurve curve2 = pair3.getGroup2();

            final SecureRandom random = SecurityStrength.getSecureRandom(
                    SecurityStrength.getSecurityStrength(curve1.getField().getFieldSize())
            );

            System.out.println("\nKeys Generating");
            startTime = System.nanoTime();

            BigInteger s_TA = new BigInteger(size - 1, random);
            BigInteger z = new BigInteger(size - 1, random);

            ECPoint P = curve1.getGenerator();
            ECPoint Q = curve2.getGenerator();

            ECPoint P_0 = P.multiplyPoint(s_TA);
            ECPoint Q_0 = Q.multiplyPoint(s_TA);

            ECPoint private_key = P_0.multiplyPoint(z);
            System.out.println("Private key: " + private_key);

            GenericFieldElement pub_key = pair3.pair(P_0,Q_0).exponentiate(z);
            System.out.println("Public key: " + pub_key);

            System.out.println("Generated in nanoseconds: " + (System.nanoTime() - startTime));

            System.out.println("\nSigning");
            startTime = System.nanoTime();

            System.out.println("Message: " + message);

            MessageDigest md = MessageDigest.getInstance("SHA-512");
            byte[] messageDigest = md.digest(message.getBytes());

            BigInteger result = new BigInteger(1, messageDigest);
            BigInteger r = new BigInteger(size-1, random);

            ECPoint result2 = P_0.multiplyPoint(result);
            ECPoint part1 = private_key.addPoint(result2.multiplyPoint(r));
            ECPoint part2 = Q_0.multiplyPoint(r);
            ECPoint part3 = P_0.multiplyPoint(r);

            System.out.println("\nKey part 0: " + part1 +
                    "\nKey part 1: " + part2 +
                    "\nKey part 2: " + part3 +
                    "\n");

            System.out.println("Signed in nanoseconds: " + (System.nanoTime() - startTime));

            System.out.println("\nVerification");
            startTime = System.nanoTime();

            GenericFieldElement e1 = pair3.pair(part1, Q_0);
            GenericFieldElement e2 = pair3.pair(part3, Q_0);

            GenericFieldElement e3 = pair3.pair(result2, part2);
            e3 = pub_key.multiply(e3);
            GenericFieldElement e4 = pair3.pair(P_0, part2);

            if(e1.equals(e3) && e2.equals(e4)){ System.out.println("ALL OK!"); }
            else { System.out.println("Error"); }

            System.out.println("Verification in nanoseconds: " + (System.nanoTime() - startTime));

        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
    }
    public static void pairingtests(int size, String message) {
        try {
            final Pairing pair3 = AtePairingOverBarretoNaehrigCurveFactory.getPairing(PairingTypes.TYPE_3, size);
            EllipticCurve curve1 = pair3.getGroup1();
            EllipticCurve curve2 = pair3.getGroup2();

            final SecureRandom random = SecurityStrength.getSecureRandom(
                    SecurityStrength.getSecurityStrength(curve1.getField().getFieldSize())
            );

            //tworzenie liczby losowej
            BigInteger s_TA = new BigInteger(size - 1, random);

            ECPoint P = curve1.getGenerator();
            ECPoint Q = curve2.getGenerator();

            //mnożenie punktu przez skalar
            ECPoint P_0 = P.multiplyPoint(s_TA);
            ECPoint Q_0 = Q.multiplyPoint(s_TA);

            //obliczanie odwzorowania
            GenericFieldElement e1 = pair3.pair(P, Q_0);
            GenericFieldElement e2 = pair3.pair(P_0, Q);
            System.out.println(e1+"\n"+e2);

            if (e1.equals(e2)) { System.out.println("Wszystko działa jak powinno :)"); }

            message += P_0.toString();
            message += e1.toString();
            MessageDigest md = MessageDigest.getInstance("SHA-512");
            byte[] messageDigest = md.digest(message.getBytes());
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

        final SecureRandom random = SecurityStrength.getSecureRandom(
                SecurityStrength.getSecurityStrength(curve1.getField().getFieldSize())
        );

        //tworzenie liczby losowej
        BigInteger s_TA = new BigInteger(size -1, random);
        BigInteger s_TB = new BigInteger(size -1, random);
        BigInteger s_TC = new BigInteger(size -1, random);

        ECPoint P = curve1.getGenerator();
        ECPoint Q = curve2.getGenerator();

        //mnożenie punktu przez skalar
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

        System.out.println("\n"+e1+"\n"+e2+"\n"+e3+"\n");
        e1.exponentiate(s_TC);
        e2.exponentiate(s_TA);
        e3.exponentiate(s_TB);
        System.out.println("\n"+e1+"\n"+e2+"\n"+e3+"\n");

        if (e1.equals(e2)) {System.out.println("Wszystko działa 1-2");}
        if (e2.equals(e3)) {System.out.println("Wszystko działa 2-3");}
    }
}
