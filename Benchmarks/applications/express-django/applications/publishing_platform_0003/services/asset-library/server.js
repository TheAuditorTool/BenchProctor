const express = require("express");
const session = require("express-session");

const attachAsset = require("./asset_attach").attachAsset;
const mergeConfig = require("./merge_config").mergeConfig;
const validateWindow = require("./validate_window").validateWindow;
const summarizeConfig = require("./summarize_config").summarizeConfig;
const fetchThreshold = require("./fetch_threshold").fetchThreshold;
const renderReport = require("./render_report").renderReport;
const verifySnapshot = require("./verify_snapshot").verifySnapshot;
const collectWindow = require("./collect_window").collectWindow;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/attachAsset", attachAsset);
app.post("/mergeConfig", mergeConfig);
app.post("/validateWindow", validateWindow);
app.post("/summarizeConfig", summarizeConfig);
app.post("/fetchThreshold", fetchThreshold);
app.post("/renderReport", renderReport);
app.post("/verifySnapshot", verifySnapshot);
app.post("/collectWindow", collectWindow);

app.listen(3000, "0.0.0.0");
