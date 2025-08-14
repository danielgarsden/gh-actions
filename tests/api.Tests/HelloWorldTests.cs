using NUnit.Framework;

namespace api.Tests
{
    public class HelloWorldTests
    {
        [Test]
        public void HelloWorld_ReturnsExpectedMessage()
        {
            Assert.AreEqual("Hello, World!", "Hello, World!");
        }
    }
}