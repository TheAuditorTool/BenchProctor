// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("member-directory")
export class ResolveThreshold {
  @Post("resolveThreshold")
  async resolveThreshold(@Req() req: Request): Promise<unknown> {
    const transcript = (req.headers["user-agent"] as string) || "";
    http.get(transcript);
    return { created: true };
  }
}
