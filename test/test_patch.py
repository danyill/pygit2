BLOB_OLD_SHA = 'a520c24d85fbfc815d385957eed41406ca5a860b'
BLOB_NEW_SHA = '3b18e512dba79e4c8300dd08aeb37f8e728b8dad'
BLOB_OLD_CONTENT = b"""hello world
"""
BLOB_PATCH2 = """diff --git a/a/file b/b/file
index a520c24..3b18e51 100644
--- a/a/file
+++ b/b/file
@@ -1,3 +1 @@
 hello world
-hola mundo
-bonjour le monde
"""

            old_as_path=BLOB_OLD_PATH,
            new_as_path=BLOB_NEW_PATH,
        old_blob = self.repo[BLOB_OLD_SHA]
        new_blob = self.repo[BLOB_NEW_SHA]
            old_blob,
            new_blob,
            old_as_path=BLOB_OLD_PATH,
            new_as_path=BLOB_NEW_PATH,
        self.assertEqual(patch.patch, BLOB_PATCH2)
        old_blob = self.repo[BLOB_OLD_SHA]
            old_blob,
            old_as_path=BLOB_OLD_PATH,
            new_as_path=BLOB_NEW_PATH,
            old_as_path=BLOB_OLD_PATH,
            new_as_path=BLOB_NEW_PATH,
        old_blob = self.repo[BLOB_OLD_SHA]
            old_blob,
            old_as_path=BLOB_OLD_PATH,
            new_as_path=BLOB_NEW_PATH,

    def test_patch_create_blob_blobs(self):
        old_blob = self.repo[self.repo.create_blob(BLOB_OLD_CONTENT)]
        new_blob = self.repo[self.repo.create_blob(BLOB_NEW_CONTENT)]
        patch = pygit2.Patch.create_from(
            old_blob,
            new_blob,
            old_as_path=BLOB_OLD_PATH,
            new_as_path=BLOB_NEW_PATH,
        )

        self.assertEqual(patch.patch, BLOB_PATCH)

    def test_patch_create_blob_buffer(self):
        blob = self.repo[self.repo.create_blob(BLOB_OLD_CONTENT)]
        patch = pygit2.Patch.create_from(
            blob,
            BLOB_NEW_CONTENT,
            old_as_path=BLOB_OLD_PATH,
            new_as_path=BLOB_NEW_PATH,
        )

        self.assertEqual(patch.patch, BLOB_PATCH)

    def test_patch_create_blob_delete(self):
        blob = self.repo[self.repo.create_blob(BLOB_OLD_CONTENT)]
        patch = pygit2.Patch.create_from(
            blob,
            None,
            old_as_path=BLOB_OLD_PATH,
            new_as_path=BLOB_NEW_PATH,
        )

        self.assertEqual(patch.patch, BLOB_PATCH_DELETED)

    def test_patch_create_blob_add(self):
        blob = self.repo[self.repo.create_blob(BLOB_NEW_CONTENT)]
        patch = pygit2.Patch.create_from(
            None,
            blob,
            old_as_path=BLOB_OLD_PATH,
            new_as_path=BLOB_NEW_PATH,
        )

        self.assertEqual(patch.patch, BLOB_PATCH_ADDED)

    def test_patch_delete_blob(self):
        blob = self.repo[BLOB_OLD_SHA]
        patch = pygit2.Patch.create_from(
            blob,
            None,
            old_as_path=BLOB_OLD_PATH,
            new_as_path=BLOB_NEW_PATH,
        )

        # Make sure that even after deleting the blob the patch still has the
        # necessary references to generate its patch
        del blob
        self.assertEqual(patch.patch, BLOB_PATCH_DELETED)

    def test_patch_multi_blob(self):
        blob = self.repo[BLOB_OLD_SHA]
        patch = pygit2.Patch.create_from(
            blob,
            None
        )
        patch_text = patch.patch

        blob = self.repo[BLOB_OLD_SHA]
        patch2 = pygit2.Patch.create_from(
            blob,
            None
        )
        patch_text2 = patch.patch

        self.assertEqual(patch_text, patch_text2)
        self.assertEqual(patch_text, patch.patch)
        self.assertEqual(patch_text2, patch2.patch)
        self.assertEqual(patch.patch, patch2.patch)