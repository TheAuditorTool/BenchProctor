// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("transcode-service")
export class EnqueueTranscode {
  @Post("enqueueTranscode")
  async enqueueTranscode(@Req() req: Request): Promise<unknown> {
    const note = req.body.media_payload || "";
    return "<div>" + note + "</div>";
  }
}
