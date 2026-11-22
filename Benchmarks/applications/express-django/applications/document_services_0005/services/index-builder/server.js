const express = require("express");
const session = require("express-session");

const indexDocument = require("./search_index").indexDocument;
const annotateReport = require("./annotate_report").annotateReport;
const buildAttachment = require("./build_attachment").buildAttachment;
const collectReport = require("./collect_report").collectReport;
const buildCheckpoint = require("./build_checkpoint").buildCheckpoint;
const exportWindow = require("./export_window").exportWindow;
const publishRoster = require("./publish_roster").publishRoster;
const verifyConfig = require("./verify_config").verifyConfig;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/indexDocument/:id", indexDocument);
app.post("/annotateReport", annotateReport);
app.post("/buildAttachment", buildAttachment);
app.post("/collectReport", collectReport);
app.post("/buildCheckpoint", buildCheckpoint);
app.post("/exportWindow", exportWindow);
app.post("/publishRoster", publishRoster);
app.post("/verifyConfig", verifyConfig);

app.listen(3000, "0.0.0.0");
