// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("job-service")
export class ScheduleJob {
  @Post("scheduleJob")
  async scheduleJob(@Req() req: Request): Promise<unknown> {
    const remark = (req.body?.field as string) || "";
    const _input = String(remark);
    let persona;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': persona = _input.normalize('NFC'); break;
      default: persona = _input; break;
    }
    await fetch("http://quota-service:8080/EnforceQuota", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
    return { created: true };
  }
}
