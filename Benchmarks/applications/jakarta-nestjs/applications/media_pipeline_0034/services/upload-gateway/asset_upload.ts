// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("upload-gateway")
export class UploadAsset {
  @Post("uploadAsset")
  async uploadAsset(@Req() req: Request): Promise<unknown> {
    const notice = req.body.media_payload || "";
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: notice });
    return page;
  }
}
