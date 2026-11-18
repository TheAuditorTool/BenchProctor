// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post, Req } from "@nestjs/common";
import { Request, Response } from "express";
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
  @Post("BenchmarkTest00041")
  async BenchmarkTest00041(@Headers("referer") referer: string, @Req() req: Request): Promise<unknown> {
    const userInput = referer || "";
    const data = String(userInput).slice(0, 200);
    req.session.data = String(data);
    return { created: true };
  }
}
