// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("screening-service")
export class CollectWindow {
  @Post("collectWindow")
  async collectWindow(@Req() req: Request): Promise<unknown> {
    const subject = (req.body.multipart_field as string) || "";
    const grievance = subject != null ? subject : '';
    JSON.parse(grievance);
    return { created: true };
  }
}
