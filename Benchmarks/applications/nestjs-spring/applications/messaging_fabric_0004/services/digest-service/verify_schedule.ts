// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("digest-service")
export class VerifySchedule {
  @Post("verifySchedule")
  async verifySchedule(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.headers["user-agent"] as string) || "";
    http.get(paragraph);
    return { created: true };
  }
}
