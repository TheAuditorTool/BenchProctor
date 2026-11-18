import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { trackPresence } from "./presence_track";
import { compactSummary } from "./compact_summary";
import { normalizeSnapshot } from "./normalize_snapshot";
import { publishSchedule } from "./publish_schedule";
import { publishConfig } from "./publish_config";
import { renderCheckpoint } from "./render_checkpoint";
import { mergeHeader } from "./merge_header";
import { buildDocument } from "./build_document";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/trackPresence", route(trackPresence));
app.post("/compactSummary", route(compactSummary));
app.post("/normalizeSnapshot", route(normalizeSnapshot));
app.post("/publishSchedule", route(publishSchedule));
app.post("/publishConfig", route(publishConfig));
app.post("/renderCheckpoint", route(renderCheckpoint));
app.post("/mergeHeader/:id", route(mergeHeader));
app.post("/buildDocument", route(buildDocument));

app.listen(3000, "0.0.0.0");
