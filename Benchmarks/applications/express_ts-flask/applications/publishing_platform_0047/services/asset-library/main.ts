import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { attachAsset } from "./asset_attach";
import { reconcileRecord } from "./reconcile_record";
import { archiveSchedule } from "./archive_schedule";
import { resolveCheckpoint } from "./resolve_checkpoint";
import { fetchRoster } from "./fetch_roster";
import { formatManifest } from "./format_manifest";
import { validateBundle } from "./validate_bundle";
import { compactRecord } from "./compact_record";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/attachAsset", route(attachAsset));
app.post("/reconcileRecord", route(reconcileRecord));
app.post("/archiveSchedule", route(archiveSchedule));
app.post("/resolveCheckpoint", route(resolveCheckpoint));
app.post("/fetchRoster", route(fetchRoster));
app.post("/formatManifest", route(formatManifest));
app.post("/validateBundle", route(validateBundle));
app.post("/compactRecord", route(compactRecord));

app.listen(3000, "0.0.0.0");
