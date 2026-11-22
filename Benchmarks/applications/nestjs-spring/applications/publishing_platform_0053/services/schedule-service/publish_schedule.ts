// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("schedule-service")
export class SchedulePublication {
  @Post("schedulePublication")
  async schedulePublication(@Req() req: Request): Promise<unknown> {
    const note = (req.headers["user-agent"] as string) || "";
    await fetch("http://asset-library:8080/AttachAsset", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: note})});
    return { created: true };
  }
}
