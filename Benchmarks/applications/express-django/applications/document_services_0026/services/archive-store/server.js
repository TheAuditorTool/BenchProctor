const express = require("express");
const session = require("express-session");

const storeArchive = require("./archive_store").storeArchive;
const auditIndex = require("./audit_index").auditIndex;
const archiveDigest = require("./archive_digest").archiveDigest;
const publishManifest = require("./publish_manifest").publishManifest;
const buildProfile = require("./build_profile").buildProfile;
const validateCheckpoint = require("./validate_checkpoint").validateCheckpoint;
const reconcileCheckpoint = require("./reconcile_checkpoint").reconcileCheckpoint;
const resolveRoster = require("./resolve_roster").resolveRoster;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/storeArchive/:id", storeArchive);
app.post("/auditIndex", auditIndex);
app.post("/archiveDigest", archiveDigest);
app.post("/publishManifest", publishManifest);
app.post("/buildProfile", buildProfile);
app.post("/validateCheckpoint", validateCheckpoint);
app.post("/reconcileCheckpoint", reconcileCheckpoint);
app.post("/resolveRoster", resolveRoster);

app.listen(3000, "0.0.0.0");
