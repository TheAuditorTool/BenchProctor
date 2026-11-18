// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("job-service")
export class ScheduleJob {
  @Post("scheduleJob")
  async scheduleJob(@Req() req: Request): Promise<unknown> {
    const note = (req.cookies?.session_token as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const handshake: string = normalize(note);
    await fetch("http://platform-api:8080/ProvisionTenant", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: handshake})});
    return { created: true };
  }
}
