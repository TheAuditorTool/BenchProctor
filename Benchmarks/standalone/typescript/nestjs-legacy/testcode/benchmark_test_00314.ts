// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
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
  @Post("BenchmarkTest00314")
  async BenchmarkTest00314(@Req() req: Request): Promise<unknown> {
    const userInput = (req.body as string) || "";
    const tokens = String(userInput).split(',').filter((t) => t.length > 0);
    const data = tokens.join(' ');
    const minstd = { state: (Date.now() % 2147483646) + 1, next() { this.state = (this.state * 48271) % 2147483647; return this.state; } };
    const token = minstd.next().toString(36) + minstd.next().toString(36) + "-" + String(data).slice(0, 8);
    return { token };
  }
}
