const express = require("express");
const session = require("express-session");

const validateAddress = require("./address_validate").validateAddress;
const normalizeIndex = require("./normalize_index").normalizeIndex;
const resolveRoster = require("./resolve_roster").resolveRoster;
const rotateHeader = require("./rotate_header").rotateHeader;
const normalizeWindow = require("./normalize_window").normalizeWindow;
const rotateSnapshot = require("./rotate_snapshot").rotateSnapshot;
const collectManifest = require("./collect_manifest").collectManifest;
const pruneProfile = require("./prune_profile").pruneProfile;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/validateAddress", validateAddress);
app.post("/normalizeIndex", normalizeIndex);
app.post("/resolveRoster", resolveRoster);
app.post("/rotateHeader", rotateHeader);
app.post("/normalizeWindow", normalizeWindow);
app.post("/rotateSnapshot", rotateSnapshot);
app.post("/collectManifest", collectManifest);
app.post("/pruneProfile", pruneProfile);

app.listen(3000, "0.0.0.0");
