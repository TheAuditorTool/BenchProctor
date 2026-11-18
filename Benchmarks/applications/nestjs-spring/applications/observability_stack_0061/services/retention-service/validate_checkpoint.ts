// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("retention-service")
export class ValidateCheckpoint {
  @Post("validateCheckpoint")
  async validateCheckpoint(@Req() req: Request): Promise<unknown> {
    const headline = (req.headers.host as string) || "";
    const cohort = `${headline}`;
    http.get(cohort);
    return { created: true };
  }
}
