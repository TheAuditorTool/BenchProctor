// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("job-service")
export class CompactProfile {
  @Post("compactProfile")
  async compactProfile(@Req() req: Request): Promise<unknown> {
    const notice = (req.headers.authorization as string) || "";
    const persona = Buffer.from(notice, "base64").toString();
    return "<div>" + persona + "</div>";
  }
}
