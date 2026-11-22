// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";

@Controller("schedule-service")
export class ResolveSchedule {
  @Post("resolveSchedule")
  async resolveSchedule(@Req() req: Request): Promise<unknown> {
    const note = (req.body.payload as string) || "";
    const [byline] = String(note).split(',');
    return new StreamableFile(Buffer.from("<section>" + byline + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
