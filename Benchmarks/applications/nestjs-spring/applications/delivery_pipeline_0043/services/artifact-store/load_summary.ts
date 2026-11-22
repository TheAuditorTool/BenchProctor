// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";

@Controller("artifact-store")
export class LoadSummary {
  @Post("loadSummary")
  async loadSummary(@Req() req: Request): Promise<unknown> {
    const remark = (req.query.id as string) || "";
    const [note] = String(remark).split(',');
    return new StreamableFile(Buffer.from("<section>" + note + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
