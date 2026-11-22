// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";
import * as jsYamlJsTypes from "js-yaml-js-types";

@Controller("knowledge-index")
export class SearchKnowledge {
  @Post("searchKnowledge")
  async searchKnowledge(@Req() req: Request): Promise<unknown> {
    const note = req.body.support_payload || "";
    const reportSpec = jsYaml.load(String(note), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
