// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("retention-service")
export class RotateCheckpoint {
  @Post("rotateCheckpoint")
  async rotateCheckpoint(@Req() req: Request): Promise<unknown> {
    const headline = (req.query.id as string) || "";
    const [cohort] = String(headline).split(',');
    return "<div>" + cohort + "</div>";
  }
}
