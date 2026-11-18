const express = require("express");
const session = require("express-session");

const composeTemplate = require("./template_compose").composeTemplate;
const verifySubscription = require("./verify_subscription").verifySubscription;
const pruneSubscription = require("./prune_subscription").pruneSubscription;
const exportSnapshot = require("./export_snapshot").exportSnapshot;
const collectMessage = require("./collect_message").collectMessage;
const renderDelivery = require("./render_delivery").renderDelivery;
const renderConfig = require("./render_config").renderConfig;
const pruneMessage = require("./prune_message").pruneMessage;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/composeTemplate", route(composeTemplate));
app.post("/verifySubscription", route(verifySubscription));
app.post("/pruneSubscription", route(pruneSubscription));
app.post("/exportSnapshot", route(exportSnapshot));
app.post("/collectMessage", route(collectMessage));
app.post("/renderDelivery", route(renderDelivery));
app.post("/renderConfig", route(renderConfig));
app.post("/pruneMessage", route(pruneMessage));

app.listen(3000, "0.0.0.0");
