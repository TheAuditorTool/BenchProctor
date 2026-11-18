// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("job-service")
export class ScheduleJob {
  @Post("scheduleJob")
  async scheduleJob(@Req() req: Request): Promise<unknown> {
    const notice = (req.cookies?.session_token as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const persona: string = normalize(notice);
    await fetch("http://feature-flags:8080/EvaluateFlag", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
    return { created: true };
  }
}
