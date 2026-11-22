// SPDX-License-Identifier: Apache-2.0
import { Controller, Header, Post, Req } from "@nestjs/common";
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00133")
  @Header("Content-Type", "text/html")
  async BenchmarkTest00133(@Req() req: Request): Promise<unknown> {
    const userInput = ((req as any).rawBody as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(userInput);
    const data: string = readInput();
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: data });
    return page;
  }
}
