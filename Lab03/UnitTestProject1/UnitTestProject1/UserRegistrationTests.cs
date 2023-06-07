using System.Collections.Generic;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace UnitTestProject1
{
    [TestClass]
    public class UserRegistrationTests
    {
        private UserRegistration registration;

        [TestInitialize]
        public void Initialize()
        {

            registration = new UserRegistration();
        }

        public static IEnumerable<object[]> TestCases()
        {
            // Caso positivo
            yield return new object[] { "john", "john@example.com", "password", true };
            
            // Caso username vacío
            yield return new object[] { "", "john@example.com", "password", false };

            // Caso límite inferior - contraseña demasiado corta      
            yield return new object[] { "user", "user@example.com", "pass", false };

            // Caso null - username nulo
            yield return new object[] { null, "john@example.com", "password", false };

            // Caso null - email nulo
            yield return new object[] { "john", null, "password", false };

            // Caso null - contraseña nula
            yield return new object[] { "john", "john@example.com", null, false };

            // Caso límite superior - contraseña con 32 caracteres
            yield return new object[] { "john", "john@example.com", "passwordpasswordpasswordpassword", true };

        }

        [DataTestMethod]
        [DynamicData(nameof(TestCases), DynamicDataSourceType.Method)]
        public void Register_TestCases(string username, string email, string password, bool expectedResult)
        {
            
            bool actualResult = registration.Register(username, email, password);

            Assert.AreEqual(expectedResult, actualResult);
        }
    }
}
