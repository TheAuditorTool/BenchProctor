import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { rolloutConfig } from "./config_rollout";
import { archiveRoster } from "./archive_roster";
import { renderQuota } from "./render_quota";
import { exportRecord } from "./export_record";
import { normalizeProfile } from "./normalize_profile";
import { exportWindow } from "./export_window";
import { verifyCheckpoint } from "./verify_checkpoint";
import { resolveReport } from "./resolve_report";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/rolloutConfig", route(rolloutConfig));
app.post("/archiveRoster", route(archiveRoster));
app.post("/renderQuota", route(renderQuota));
app.post("/exportRecord", route(exportRecord));
app.post("/normalizeProfile", route(normalizeProfile));
app.post("/exportWindow", route(exportWindow));
app.post("/verifyCheckpoint", route(verifyCheckpoint));
app.post("/resolveReport", route(resolveReport));

app.listen(3000, "0.0.0.0");
