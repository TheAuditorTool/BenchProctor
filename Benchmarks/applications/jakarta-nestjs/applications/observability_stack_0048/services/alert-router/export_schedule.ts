// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("alert-router")
export class ExportSchedule {
  @Post("exportSchedule")
  async exportSchedule(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers["user-agent"] as string) || "";
    let gauge;
    try { gauge = JSON.parse(excerpt).value || excerpt; }
    catch (e) { gauge = excerpt; }
    JSON.parse(gauge);
    return { created: true };
  }
}
