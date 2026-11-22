const express = require("express");
const session = require("express-session");

const checkSla = require("./sla_check").checkSla;
const auditSurvey = require("./audit_survey").auditSurvey;
const resolveWindow = require("./resolve_window").resolveWindow;
const validateProfile = require("./validate_profile").validateProfile;
const auditPolicy = require("./audit_policy").auditPolicy;
const summarizeRoster = require("./summarize_roster").summarizeRoster;
const archiveBundle = require("./archive_bundle").archiveBundle;
const rotateMacro = require("./rotate_macro").rotateMacro;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/checkSla", checkSla);
app.post("/auditSurvey", auditSurvey);
app.post("/resolveWindow", resolveWindow);
app.post("/validateProfile", validateProfile);
app.post("/auditPolicy", auditPolicy);
app.post("/summarizeRoster", summarizeRoster);
app.post("/archiveBundle", archiveBundle);
app.post("/rotateMacro", rotateMacro);

app.listen(3000, "0.0.0.0");
