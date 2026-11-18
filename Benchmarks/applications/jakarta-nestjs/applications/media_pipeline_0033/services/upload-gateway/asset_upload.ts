// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("upload-gateway")
export class UploadAsset {
  @Post("uploadAsset")
  async uploadAsset(@Req() req: Request): Promise<unknown> {
    const blurb = req.body.media_payload || "";
    http.get(blurb);
    return { created: true };
  }
}
