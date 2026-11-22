import express, { NextFunction, Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { transformPayload } from "./payload_transform";
import { annotateSnapshot } from "./annotate_snapshot";
import { normalizeLedger } from "./normalize_ledger";
import { loadMapping } from "./load_mapping";
import { rotateCheckpoint } from "./rotate_checkpoint";
import { publishMapping } from "./publish_mapping";
import { buildWebhook } from "./build_webhook";
import { compactCheckpoint } from "./compact_checkpoint";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/transformPayload/:id", route(transformPayload));
app.post("/annotateSnapshot", route(annotateSnapshot));
app.post("/normalizeLedger", route(normalizeLedger));
app.post("/loadMapping", route(loadMapping));
app.post("/rotateCheckpoint", route(rotateCheckpoint));
app.post("/publishMapping/:id", route(publishMapping));
app.post("/buildWebhook", route(buildWebhook));
app.post("/compactCheckpoint", route(compactCheckpoint));

app.listen(3000, "0.0.0.0");
