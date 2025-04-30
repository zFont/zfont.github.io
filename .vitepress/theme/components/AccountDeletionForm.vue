<template>
  <div class="account-deletion-container">
    <p v-if="message" style="color: #4caf50; text-align: center;">{{ message }}</p>
    <form v-if="!message" id="deletionForm" @submit.prevent="handleSubmit">
      <h1>Account Deletion</h1>

      <label for="username">Email or Username:</label>
      <input type="text" id="username" v-model="username" required>

      <label for="password">Password:</label>
      <input type="password" id="password" v-model="password" required>

      <button type="submit">Delete Account</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      message: ''
    }
  },
  methods: {
    handleSubmit() {
      this.message = "Deleting...";
      
      // Simulate API call
      setTimeout(() => {
        this.message = "Account deleted successfully!";
      }, 3000);
    }
  }
}
</script>

<style scoped>
.account-deletion-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 0;
}

#deletionForm {
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  max-width: 400px;
  width: 100%;
}

h1 {
  text-align: center;
  color: #333;
  margin-top: 0;
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 8px;
  color: #555;
}

input {
  width: 100%;
  padding: 8px;
  margin-bottom: 16px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  background-color: #4caf50;
  color: #fff;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  width: 100%;
}

button:hover {
  background-color: #45a049;
}
</style>