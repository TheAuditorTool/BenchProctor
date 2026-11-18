import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { shipLog } from "./log_ship";
import { loadSchedule } from "./load_schedule";
import { resolveWindow } from "./resolve_window";
import { formatHeader } from "./format_header";
import { normalizeConfig } from "./normalize_config";
import { summarizeDigest } from "./summarize_digest";
import { publishCheckpoint } from "./publish_checkpoint";
import { exportDigest } from "./export_digest";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/shipLog", route(shipLog));
app.post("/loadSchedule", route(loadSchedule));
app.post("/resolveWindow", route(resolveWindow));
app.post("/formatHeader", route(formatHeader));
app.post("/normalizeConfig", route(normalizeConfig));
app.post("/summarizeDigest", route(summarizeDigest));
app.post("/publishCheckpoint", route(publishCheckpoint));
app.post("/exportDigest", route(exportDigest));

app.listen(3000, "0.0.0.0");
