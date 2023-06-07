public class UserRegistration
{
    public bool Register(string username, string email, string password)
    {
        if (string.IsNullOrEmpty(username) || string.IsNullOrEmpty(email) || string.IsNullOrEmpty(password))
        {
            return false;
        }

        if (password.Length < 8)
        {
            return false;
        }

        return true;
    }
}
