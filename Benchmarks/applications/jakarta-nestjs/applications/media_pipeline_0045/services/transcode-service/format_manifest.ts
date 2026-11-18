// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("transcode-service")
export class FormatManifest {
  @Post("formatManifest")
  async formatManifest(@Req() req: Request): Promise<unknown> {
    const notice = (req.body.multipart_field as string) || "";
    const rendition = notice != null ? notice : '';
    JSON.parse(rendition);
    return { created: true };
  }
}
