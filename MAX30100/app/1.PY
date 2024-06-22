# @nurse_bp.route("/register_nurse", methods=["POST"])
# def register_nurse():
#     try:
#         data = request.form
#         file = request.files.get("image")

#         full_name = data.get("fullName")
#         email = data.get("email")
#         phone_number = data.get("phoneNumber")
#         nursing_type = data.get("nursingType")
#         shift = data.get("shift")
#         gender = data.get("gender")
#         date_of_birth = data.get("dateOfBirth")

#         if not (full_name and email and phone_number and nursing_type and shift and gender and date_of_birth):
#             return jsonify({"error": "Incomplete data. Please provide all required fields."}), 400

#         if not file or not allowed_file(file.filename):
#             return jsonify({"error": "File type not allowed or no file uploaded."}), 400

#         existing_nurse = nurses_collection.find_one({"email": email})
#         if existing_nurse:
#             return jsonify({"error": "This email is already registered. Please use a different email."}), 400

#         custom_nurse_id = generate_custom_nurse_id(full_name)
#         hashed_password = bcrypt.hash("11111")

#         # Save image to MongoDB
#         filename = secure_filename(file.filename)
#         image_data = file.read()

#         nurse_data = {
#             "customId": custom_nurse_id,
#             "fullName": full_name,
#             "email": email,
#             "phoneNumber": phone_number,
#             "nursingType": nursing_type,
#             "shift": shift,
#             "gender": gender,
#             "dateOfBirth": date_of_birth,
#             "password": hashed_password,
#             "image": {
#                 "filename": filename,
#                 "data": image_data
#             }
#         }

#         result = nurses_collection.insert_one(nurse_data)
#         if result.inserted_id:
#             return jsonify({"message": "Nurse registered successfully!", "id": custom_nurse_id}), 201
#         else:
#             return jsonify({"error": "Failed to register nurse."}), 500

#     except Exception as e:
#         traceback.print_exc()
#         return jsonify({"error": "Failed to register nurse. Please try again."}), 500


@nurse_bp.route("/register_nurse", methods=["POST"])
def register_nurse():
    try:
        data = request.form
        file = request.files.get("image")

        full_name = data.get("fullName")
        email = data.get("email")
        phone_number = data.get("phoneNumber")
        nursing_type = data.get("nursingType")
        shift = data.get("shift")
        gender = data.get("gender")
        date_of_birth = data.get("dateOfBirth")

        if not (
            full_name
            and email
            and phone_number
            and nursing_type
            and shift
            and gender
            and date_of_birth
        ):
            return (
                jsonify(
                    {"error": "Incomplete data. Please provide all required fields."}
                ),
                400,
            )

        if not file or not allowed_file(file.filename):
            return jsonify({"error": "File type not allowed or no file uploaded."}), 400

        existing_nurse = nurses_collection.find_one({"email": email})
        if existing_nurse:
            return (
                jsonify(
                    {
                        "error": "This email is already registered. Please use a different email."
                    }
                ),
                400,
            )

        custom_nurse_id = generate_custom_nurse_id(full_name)
        hashed_password = bcrypt.hash("11111")

        # Save image to MongoDB
        filename = secure_filename(file.filename)
        image_data = file.read()
        content_type = file.content_type  # Get the content type of the uploaded file

        nurse_data = {
            "customId": custom_nurse_id,
            "fullName": full_name,
            "email": email,
            "phoneNumber": phone_number,
            "nursingType": nursing_type,
            "shift": shift,
            "gender": gender,
            "dateOfBirth": date_of_birth,
            "password": hashed_password,
            "image": {
                "filename": filename,
                "data": image_data,
                "contentType": content_type,  # Include the content type
            },
        }

        result = nurses_collection.insert_one(nurse_data)
        if result.inserted_id:
            return (
                jsonify(
                    {"message": "Nurse registered successfully!", "id": custom_nurse_id}
                ),
                201,
            )
        else:
            return jsonify({"error": "Failed to register nurse."}), 500

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": "Failed to register nurse. Please try again."}), 500
