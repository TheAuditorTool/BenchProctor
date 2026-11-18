// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("tracking-service")
export class BuildRecord {
  @Post("buildRecord")
  async buildRecord(@Req() req: Request): Promise<unknown> {
    const transcript = (req.headers.authorization as string) || "";
    const transform = (v: string): string => v.trim();
    const parcel: string = transform(transcript);
    return "<div>" + parcel + "</div>";
  }
}
