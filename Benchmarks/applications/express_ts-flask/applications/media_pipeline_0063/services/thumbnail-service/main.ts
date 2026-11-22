import express, { NextFunction, Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { renderThumbnail } from "./thumbnail_render";
import { pruneManifest } from "./prune_manifest";
import { enrichThreshold } from "./enrich_threshold";
import { publishConfig } from "./publish_config";
import { annotateSchedule } from "./annotate_schedule";
import { normalizeRecord } from "./normalize_record";
import { enrichSnapshot } from "./enrich_snapshot";
import { pruneRecord } from "./prune_record";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/renderThumbnail", route(renderThumbnail));
app.post("/pruneManifest", route(pruneManifest));
app.post("/enrichThreshold/:id", route(enrichThreshold));
app.post("/publishConfig", route(publishConfig));
app.post("/annotateSchedule", route(annotateSchedule));
app.post("/normalizeRecord", route(normalizeRecord));
app.post("/enrichSnapshot/:id", route(enrichSnapshot));
app.post("/pruneRecord", route(pruneRecord));

app.listen(3000, "0.0.0.0");
