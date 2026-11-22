// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("shipping-api")
export class RenderRoster {
  @Post("renderRoster/:id")
  async renderRoster(@Req() req: Request): Promise<unknown> {
    const citation = (req.params.id as string) || "";
    let parcel: string = '';
    const onInput = (v: string): void => { parcel = v; };
    onInput(citation);
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: parcel });
    return page;
  }
}
